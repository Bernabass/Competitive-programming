import javax.swing.JOptionPane;
public class test{
    public static void main(String[] args){
        String input1 = JOptionPane.showInputDialog("Enter the value of x: ");
        String input2 = JOptionPane.showInputDialog("Enter the value of y: ");
        int x = Integer.parseInt(input1);
        int y = Integer.parseInt(input2);
        int z;
        JOptionPane.showMessageDialog(null,"The value of z is "+ (z = x > y? 1: 20));
    }
}