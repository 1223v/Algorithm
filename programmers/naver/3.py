# import java.util.*;
#
# public class IPAddressAPI {
#     public int[] solution(String[] ip_addresses, String[] registered_list, String[] banned_list) {
#         // 결과를 저장할 배열
#         int[] responseCodes = new int[ip_addresses.length];
#
#         // Set으로 효율적인 검색
#         Set<String> registeredSet = new HashSet<>(Arrays.asList(registered_list));
#         Set<String> bannedSet = new HashSet<>(Arrays.asList(banned_list));
#
#         // IP 주소 처리
#         for (int i = 0; i < ip_addresses.length; i++) {
#             String ip = ip_addresses[i];
#
#             // 1. 유효성 검사
#             if (!isValidIPv4(ip)) {
#                 responseCodes[i] = 1; // 규격에 맞지 않는 IP
#                 continue;
#             }
#
#             // 2. 등록된 IP인지 확인
#             if (registeredSet.contains(ip)) {
#                 responseCodes[i] = 0; // 등록된 IP
#                 continue;
#             }
#
#             // 3. 차단된 IP인지 확인
#             if (bannedSet.contains(ip)) {
#                 responseCodes[i] = 3; // 차단된 IP
#                 continue;
#             }
#
#             // 4. 등록/차단되지 않은 IP
#             responseCodes[i] = 2;
#         }
#
#         return responseCodes;
#     }
#
#     // IPv4 유효성 검사 함수
#     private boolean isValidIPv4(String ip) {
#         // "."으로 분리
#         String[] parts = ip.split("\\.");
#         if (parts.length != 4) return false;
#
#         for (String part : parts) {
#             // 숫자가 아닌 경우 거부
#             if (!isNumeric(part)) return false;
#
#             // 숫자로 변환
#             int num = Integer.parseInt(part);
#
#             // 0~255 범위 확인
#             if (num < 0 || num > 255) return false;
#
#             // 0으로 시작하는 경우 확인 (0인 경우는 "0"이어야만 함)
#             if (part.startsWith("0") && part.length() > 1) return false;
#         }
#
#         return true;
#     }
#
#     // 문자열이 숫자인지 확인
#     private boolean isNumeric(String str) {
#         for (char c : str.toCharArray()) {
#             if (!Character.isDigit(c)) {
#                 return false;
#             }
#         }
#         return true;
#     }
#
#     public static void main(String[] args) {
#         IPAddressAPI api = new IPAddressAPI();
#
#         // 입력 예시 1
#         String[] ip_addresses1 = {"123.023.123.123", "1.1.1.12", "119.123.45.39", "127.0.0.1"};
#         String[] registered_list1 = {"119.123.45.39"};
#         String[] banned_list1 = {"1.1.1.12"};
#         System.out.println(Arrays.toString(api.solution(ip_addresses1, registered_list1, banned_list1))); // [1, 3, 0, 2]
#
#         // 입력 예시 2
#         String[] ip_addresses2 = {"115.86.56.15", "123.12.2.1"};
#         String[] registered_list2 = {"115.86.56.15"};
#         String[] banned_list2 = {"1.1.1.12"};
#         System.out.println(Arrays.toString(api.solution(ip_addresses2, registered_list2, banned_list2))); // [0, 1]
#     }
# }