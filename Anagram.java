import java.util.Scanner;

public class Anagram {

    static boolean isAnagram(String a, String b) {
        // Complete the function
        boolean Flag = true;
        if(a.length()!=b.length()){
            return false;
        }
        else{
            a = a.toLowerCase();
            b = b.toLowerCase();
            for(int i=0;i<a.length();i++){
                char temp = a.charAt(i);
                int count1= 0;
                int count2= 0;
                for(int j=0;j<a.length();j++){
                    char x = a.charAt(j);
                    if(temp == x){
                        count1++;
                    }
                }
                for(int j=0;j<b.length();j++){
                    char y = b.charAt(j);
                    if(temp == y){
                        count2++;
                    }
                }
                if(count1!=count2){
                    Flag = false;
                }
                
                
            }
            return Flag;
        }
    }

    public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}
