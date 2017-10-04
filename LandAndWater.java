import java.io.*;
import java.util.*;

    // Prompt: 
    // Detect whether given an initial speed if you can cross the path 
    // that consists of water and land. You can increase your speed by 1, 
    // decrease your speed by 1, or not increase or decrease on each movement.

    // Arguments:
    // path -- Array: an array representation of a path that consists of land 
    // "L" and water "W"
    // speed -- Int: the starting speed at which you move

    // Returns:
    // outcome -- Boolean: whether it is possible or not to cross the river 
    // given the initial speed

class LandAndWater {
    public static void main(String[] args) {
        String[] path1 = {"L", "L", "W", "L"}; // True
        String[] path2 = {"L", "L", "W", "W", "L", "L"}; // False
        String[] path3 = {"L", "L", "L", "L", "L", "L", "L", "W", "W", "W", "L"}; // True

        HashMap<Integer, HashMap<Integer, Boolean>> memo = new HashMap<Integer, HashMap<Integer, Boolean>>();
        boolean result = crossPath(path3, 0, 1, memo);
        System.out.println(result);
    }

    public static boolean crossPath(String[] path, int start, int speed, 
                                    HashMap<Integer, HashMap<Integer, Boolean>> memo) {
        if (memo.containsKey(start) && memo.get(start).containsKey(speed)) {
            System.out.println("MEMO start, speed: " + start + "," + speed);
            return memo.get(start).get(speed);
        } else if (start >= path.length) {
            return true;
        } else if (speed < 1) {
            return false;
        } else if (path[start] == "W") {
            return false;
        }
        System.out.println("start, speed: " + start + "," + speed);
        boolean result = crossPath(path, start + speed, speed, memo) ||
                         crossPath(path, start + speed, speed + 1, memo) ||
                         crossPath(path, start + speed, speed - 1, memo);
        if (memo.containsKey(start)) {
            HashMap<Integer, Boolean> innerMemo = memo.get(start);
            innerMemo.put(speed, result);
            memo.put(start, innerMemo);
        } else {
            HashMap<Integer, Boolean> innerMemo = new HashMap<Integer, Boolean>();
            innerMemo.put(speed, result);
            memo.put(start, innerMemo);
        }
        return result;
    }
}

// some help on hashmap of hashmap:
// https://stackoverflow.com/questions/14677993/how-to-create-a-hashmap-with-two-keys-key-pair-value
