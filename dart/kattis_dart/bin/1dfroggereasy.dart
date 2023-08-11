import 'dart:io';

void main(List<String> arguments) {
  String? line;
  line = stdin.readLineSync();
  final List<int> nums = line!.split(' ').map(int.parse).toList();
  final int s = nums[1];
  final int m = nums[2];
  line = stdin.readLineSync();
  final List<int> board = line!.split(' ').map(int.parse).toList();
  final Set<int> been = {};
  int at = s - 1;
  int hops = 0;
  while (true) {
    if (at < 0) {
      print('left\n$hops');
      return;
    }
    if (at >= board.length) {
      print('right\n$hops');
      return;
    }
    if (board[at] == m) {
      print('magic\n$hops');
      return;
    }
    if (been.contains(at)) {
      print('cycle\n$hops');
      return;
    }
    been.add(at);
    at += board[at];
    hops++;
  }
}
