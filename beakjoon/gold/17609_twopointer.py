import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    s = input().rstrip()
    chk = 0
    chk2 = 0
    if s == s[::-1]:
        print(0)
    # 짝수
    elif len(s) % 2 == 0:
        start = 0
        end = len(s)-1
        while start <= end:

            if s[start] != s[end]:
                if s[start+1] == s[end]:
                    end -= 1
                    start += 2
                    chk += 1

                elif s[start] == s[end+1]:
                    end -= 2
                    start += 1
                    chk += 1
                else:
                    chk2 = 1
                    break

            elif s[start] == s[end]:
                start += 1
                end -= 1



    # 홀수
    elif len(s) % 2 == 1:
           target_index= len(s) // 2
           start = 0
           end = len(s)-1
           while start != target_index and end != target_index:
               if s[start] != s[end]:
                   if s[start + 1] == s[end]:
                       end -= 1
                       start += 2
                       chk += 1



                   elif s[start] == s[end + 1]:
                       end -= 2
                       start += 1
                       chk += 1
                   else:
                       chk2 = 1
                       break

               elif s[start] == s[end]:
                   start += 1
                   end -= 1


    if chk == 1:

        print(1)

    else:
        print(chk)