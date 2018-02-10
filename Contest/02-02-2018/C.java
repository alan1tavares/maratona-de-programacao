import java.io.*; 
import java.math.BigInteger;
class Main{
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String n;
        while((n = br.readLine()) != null) {
            BigInteger big = new BigInteger(n);
            String res = big.pow(Integer.parseInt(n))+"";
            
            
            if(n.equals(res.substring(res.length() - n.length())))
                System.out.println("SIM");
            else
                System.out.println("NAO");
        }
    }
}