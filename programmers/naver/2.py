# import java.util.*;
# import java.io.*;
#
# public class a {
#     public static void main(String[] args) throws Exception {
#         List<String> a = new ArrayList<>();
#         List<String> b = new ArrayList<>();
#         a.add("123 gate502 like");
#         a.add("123 gate502 s");
#         a.add("123 cookie52 s");
#         a.add("123 cookie52 like");
#         a.add("123 cookie52 g");
#         a.add("123 cookie52 g");
#         a.add("123 gate502 g");
#         a.add("123 coupone like");
#         a.add("123 coupone g");
#
#         b.add("s");
#         b.add("like");
#         b.add("g");
#
#         System.out.println(solution(a, b));
#     }
#     public static List<String> solution(List<String> logs, List<String> events){
#         Set<String> sol = new HashSet<>();
#         Map<String, Integer> usersEvent = new HashMap<>();
#         int eventSize = events.size();
#
#         for(String log : logs){
#             String[] values = log.split(" ");
#             if(sol.contains(values[1])) continue;
#             Integer userEvent = usersEvent.get(values[1]);
#             if(userEvent == null){
#                 if(values[2].equals(events.get(0))){
#                     usersEvent.put(values[1], 1);
#                 }
#                 else sol.add(values[1]);
#             }
#             else if(userEvent >= eventSize) {
#                 sol.add(values[1]);
#             }
#             else {
#                 if(values[2].equals(events.get(userEvent))){
#                     usersEvent.put(values[1], userEvent+1);
#                 }
#                 else{
#                     sol.add(values[1]);
#                 }
#             }
#         }
#
#         List<String> sortedSol = new ArrayList<>(sol);
#         Collections.sort(sortedSol);
#
#         return new ArrayList<>(sortedSol);
#     }
# }