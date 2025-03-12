import pandas as pd
import pymysql
import numpy as np

# Load the CSV file
file_path = r"C:\Users\조현식\Desktop\학교기본정보(고)_전체.csv"
data = pd.read_csv(file_path)

# Replace NaN values with None for MySQL compatibility
data = data.replace({pd.NA: None, np.nan: None})

# Remove duplicates for unique subqueries
data = data.drop_duplicates(subset=['교육지원청', '시도교육청'], keep='first')

# Function to handle NULL values in SQL
def format_value(value, is_date=False):
    if value in [None, '', 'NaT']:
        return 'NULL'
    if is_date:
        try:
            pd.to_datetime(value)  # Validate date format
            return f"'{value}'"  # Return as quoted string for SQL
        except:
            return 'NULL'
    return f"'{value}'"

# Database connection configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "12345678",
    "database": "example_database",
    "charset": "utf8mb4"
}

# Function to check for duplicates in a table
def check_duplicate(cursor, table, column, value):
    cursor.execute(f"SELECT COUNT(*) FROM {table} WHERE {column} = {format_value(value)};")
    return cursor.fetchone()[0] > 0

# Function to insert data into the database
def insert_data_to_db(data, db_config):
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    # Initialize lists to store SQL statements
    sql_cityeduoffice = []
    sql_region = []
    sql_districteduoffice = []
    sql_school = []
    sql_schooladdress = []
    sql_schoolcontact = []

    try:
        # Insert into cityeduoffice
        city_edu_offices = data['시도교육청'].drop_duplicates()
        for office in city_edu_offices:
            if office is None or office.strip() == '':
                print(f"Skipping empty cityeduoffice: {office}")
                continue
            if not check_duplicate(cursor, 'cityeduoffice', 'name', office):
                sql = f"INSERT INTO cityeduoffice (name) VALUES ({format_value(office)});"
                cursor.execute(sql)
                sql_cityeduoffice.append(sql)

        # Insert into region
        regions = data['지역'].drop_duplicates()
        for region in regions:
            if region is None or region.strip() == '':
                print(f"Skipping empty region: {region}")
                continue
            if not check_duplicate(cursor, 'region', 'name', region):
                sql = f"INSERT INTO region (name) VALUES ({format_value(region)});"
                cursor.execute(sql)
                sql_region.append(sql)

        # Insert into districteduoffice
        district_edu_offices = data[['교육지원청', '시도교육청']].drop_duplicates()
        for _, row in district_edu_offices.iterrows():
            if row['교육지원청'] is None or row['시도교육청'] is None or row['교육지원청'].strip() == '' or row['시도교육청'].strip() == '':
                print(f"Skipping empty districteduoffice: {row['교육지원청']} / {row['시도교육청']}")
                continue
            if not check_duplicate(cursor, 'districteduoffice', 'name', row['교육지원청']):
                sql = f"""
                    INSERT INTO districteduoffice (name, city_office_id)
                    VALUES ({format_value(row['교육지원청'])}, 
                            (SELECT DISTINCT city_office_id FROM cityeduoffice WHERE name = {format_value(row['시도교육청'])} LIMIT 1));
                """
                cursor.execute(sql)
                sql_districteduoffice.append(sql.strip())

        # Insert into school
        school_codes_inserted = []
        for _, row in data.iterrows():
            if row['정보공시 학교코드'] is None or row['정보공시 학교코드'].strip() == '':
                print(f"Skipping school with empty school_code: {row['학교명']}")
                continue

            cursor.execute(f"""
                SELECT DISTINCT district_office_id FROM districteduoffice WHERE name = {format_value(row['교육지원청'])} LIMIT 1
            """)
            district_office_id = cursor.fetchone()

            cursor.execute(f"""
                SELECT DISTINCT region_id FROM region WHERE name = {format_value(row['지역'])} LIMIT 1
            """)
            region_id = cursor.fetchone()

            if district_office_id is None or region_id is None:
                print(f"Skipping school {row['학교명']} due to unresolved foreign keys.")
                continue

            if not check_duplicate(cursor, 'school', 'school_code', row['정보공시 학교코드']):
                sql = f"""
                    INSERT INTO school (
                        school_code, district_office_id, region_id, school_name, school_grade_code,
                        founding_type, school_feature, is_branch_school, establishing_type,
                        day_night_type, anniversary_date, founding_date, gender_type,
                        is_closed, closed_date, is_suspended
                    ) VALUES (
                        {format_value(row['정보공시 학교코드'])}, {district_office_id[0]}, {region_id[0]}, {format_value(row['학교명'])}, {format_value(row['학교급코드'])},
                        {format_value(row['설립구분'])}, {format_value(row['학교특성'])}, {format_value(row['분교여부'])}, {format_value(row['설립유형'])}, {format_value(row['주야구분'])},
                        {format_value(row['개교기념일'], is_date=True)}, {format_value(row['설립일'], is_date=True)}, {format_value(row['남녀공학 구분'])}, {format_value(row['폐교여부'])},
                        {format_value(row['폐교일자'], is_date=True)}, {format_value(row['휴교여부'])}
                    );
                """
                cursor.execute(sql)
                sql_school.append(sql.strip())
                school_codes_inserted.append(row['정보공시 학교코드'])

        # Insert into schooladdress
        for _, row in data.iterrows():
            if row['정보공시 학교코드'] not in school_codes_inserted:
                print(f"Skipping schooladdress for {row['정보공시 학교코드']} as it does not exist in school table.")
                continue

            if not row['학교도로명 주소'] or not row['우편번호']:
                print(f"Skipping schooladdress for {row['정보공시 학교코드']} due to missing address data.")
                continue

            sql = f"""
                INSERT INTO schooladdress (
                    school_code, legal_dong_code, old_address, old_address_det,
                    old_zipcode, road_zipcode, road_address, road_address_det,
                    latitude, longitude
                ) VALUES (
                    {format_value(row['정보공시 학교코드'])}, {format_value(row['법정동코드'])}, {format_value(row['주소내역'])}, {format_value(row['상세주소내역'])},
                    {format_value(row['우편번호'])}, {format_value(row['학교도로명 우편번호'])}, {format_value(row['학교도로명 주소'])}, {format_value(row['학교도로명 상세주소'])},
                    {row['위도'] if row['위도'] is not None else 'NULL'}, {row['경도'] if row['경도'] is not None else 'NULL'}
                );
            """
            cursor.execute(sql)
            sql_schooladdress.append(sql.strip())

        # Insert into schoolcontact
        for _, row in data.iterrows():
            if row['정보공시 학교코드'] not in school_codes_inserted:
                print(f"Skipping schoolcontact for {row['정보공시 학교코드']} as it does not exist in school table.")
                continue

            if not row['전화번호'] or not row['팩스번호']:
                print(f"Skipping schoolcontact for {row['정보공시 학교코드']} due to missing contact data.")
                continue

            sql = f"""
                INSERT INTO schoolcontact (
                    school_code, phone, fax, homepage
                ) VALUES (
                    {format_value(row['정보공시 학교코드'])}, {format_value(row['전화번호'])}, {format_value(row['팩스번호'])}, {format_value(row['홈페이지 주소'])}
                );
            """
            cursor.execute(sql)
            sql_schoolcontact.append(sql.strip())

        # Commit the transaction
        connection.commit()
        print("Data inserted successfully!")
    except Exception as e:
        connection.rollback()
        print("Error occurred:", e)
    finally:
        cursor.close()
        connection.close()


# Call the function to insert data into the database
insert_data_to_db(data, db_config)
