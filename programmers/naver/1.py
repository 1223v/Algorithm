# import java.util.*;
# import java.io.*;
#
# public class a {
#     public static void main(String[] args) throws Exception {
#
#         System.out.println(solution("URLLDRLR"));
#         System.out.println(solution("RLDU"));
#         System.out.println(solution("URDLDRULDLRUDLU"));
#     }
#     public static int solution(String s){
#         int sol = 0;
#         int[][][] cmd = new int[s.length()+5][s.length()+5][2];
#
#         // i: 명령어 index, 범위 끝
#         for(int i = 0; i < s.length(); i++){
#             char c = s.charAt(i);
#             //j: 범위 시작
#             for(int j = 0; j <= i; j++){
#                 if(i != 0) {
#                     cmd[j][i][0] = cmd[j][i-1][0];
#                     cmd[j][i][1] = cmd[j][i-1][1];
#                 }
#                 if(c == 'U'){
#                     cmd[j][i][0]++;
#                 }
#                 if(c == 'D'){
#                     cmd[j][i][0]--;
#                 }
#                 if(c == 'R'){
#                     cmd[j][i][1]++;
#                 }
#                 if(c == 'L'){
#                     cmd[j][i][1]--;
#                 }
#                 if(cmd[j][i][0] == 0 && cmd[j][i][1] == 0) sol++;
#             }
#         }
#
#         return sol;
#     }
# }
