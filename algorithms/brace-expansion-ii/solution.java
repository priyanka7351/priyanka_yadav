import java.util.*;

class Solution {

    int index = 0;

    public List<String> braceExpansionII(String expression) {

        Set<String> result = parse(expression);

        List<String> ans = new ArrayList<>(result);
        Collections.sort(ans);

        return ans;
    }

    private Set<String> parse(String s) {

        Set<String> result = new HashSet<>();
        Set<String> current = new HashSet<>();

        current.add("");

        while (index < s.length() && s.charAt(index) != '}') {

            char ch = s.charAt(index);

            Set<String> part;

            if (ch == '{') {

                index++; // skip {

                part = parse(s);

                index++; // skip }

            } 
            else {

                part = new HashSet<>();
                part.add(String.valueOf(ch));

                index++;
            }

            // Concatenation
            Set<String> next = new HashSet<>();

            for (String a : current) {
                for (String b : part) {
                    next.add(a + b);
                }
            }

            current = next;

            // Union
            if (index < s.length() && s.charAt(index) == ',') {

                result.addAll(current);

                current.clear();
                current.add("");

                index++;
            }
        }

        result.addAll(current);

        return result;
    }
}