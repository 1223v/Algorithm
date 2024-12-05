# import java.util.PriorityQueue;
# import java.util.Arrays;
#
# public class Solution {
#
#     public static int solution(int[][] board, int c) {
#         int n = board.length;
#         int m = board[0].length;
#
#         // 시작점과 끝점 찾기
#         int[] start = new int[2];
#         int[] end = new int[2];
#         for (int i = 0; i < n; i++) {
#             for (int j = 0; j < m; j++) {
#                 if (board[i][j] == 2) {
#                     start[0] = i;
#                     start[1] = j;
#                 }
#                 if (board[i][j] == 3) {
#                     end[0] = i;
#                     end[1] = j;
#                 }
#             }
#         }
#
#         // 방향: 상, 하, 좌, 우
#         int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
#
#         // 거리 배열 초기화 (무한대로 초기화)
#         int[][] dist = new int[n][m];
#         for (int[] row : dist) {
#             Arrays.fill(row, Integer.MAX_VALUE);
#         }
#         dist[start[0]][start[1]] = 0;
#
#         // 우선순위 큐 (Dijkstra 알고리즘용)
#         PriorityQueue<Node> pq = new PriorityQueue<>();
#         pq.offer(new Node(start[0], start[1], 0));
#
#         while (!pq.isEmpty()) {
#             Node current = pq.poll();
#             int cost = current.cost;
#             int x = current.x;
#             int y = current.y;
#
#             // 목적지에 도달했을 경우
#             if (x == end[0] && y == end[1]) {
#                 return cost;
#             }
#
#             // 이미 더 짧은 경로를 찾은 경우 무시
#             if (cost > dist[x][y]) {
#                 continue;
#             }
#
#             // 인접한 칸 탐색
#             for (int[] dir : directions) {
#                 int nx = x + dir[0];
#                 int ny = y + dir[1];
#
#                 // 경계 체크
#                 if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
#                     int newCost;
#                     if (board[nx][ny] == 0 || board[nx][ny] == 3) {
#                         newCost = cost + 1;
#                     } else if (board[nx][ny] == 1) {
#                         newCost = cost + c + 1;
#                     } else {
#                         continue; // 시작점을 다시 방문하지 않음
#                     }
#
#                     // 더 짧은 경로 발견 시 업데이트
#                     if (newCost < dist[nx][ny]) {
#                         dist[nx][ny] = newCost;
#                         pq.offer(new Node(nx, ny, newCost));
#                     }
#                 }
#             }
#         }
#
#         // 목적지에 도달 불가능한 경우
#         return -1;
#     }
#
#     // Node 클래스 (우선순위 큐를 위한 비교 메서드 포함)
#     static class Node implements Comparable<Node> {
#         int x, y, cost;
#
#         Node(int x, int y, int cost) {
#             this.x = x;
#             this.y = y;
#             this.cost = cost;
#         }
#
#         @Override
#         public int compareTo(Node other) {
#             return Integer.compare(this.cost, other.cost);
#         }
#     }
#
#     public static void main(String[] args) {
#         // 테스트 케이스
#         int[][] board = {
#             {0, 1, 0, 0, 0},
#             {0, 1, 0, 1, 0},
#             {2, 0, 0, 1, 3},
#             {0, 1, 0, 0, 0}
#         };
#         int c = 5;
#
#         System.out.println(solution(board, c)); // 결과 출력
#     }
# }
