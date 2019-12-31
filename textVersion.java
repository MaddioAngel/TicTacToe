import java.util.*;  
public class textVersion{

    static Character[][] board = new Character[3][3];
    static Scanner scan = new Scanner(System.in);  

    static{ //Creates the game board
        for(int i = 0; i <3; i++){
            for(int j = 0; j<3; j++){
                board[i][j] = '-';
            }
        }

    }
    
    public static void main(String[] args){
    System.out.println("Welcome to TicTacToe");
    System.out.println("-----");
    
    while(!checkWin()){
        if(!oWin()){
            printBoard();
            xPlayer();
        }
        if(!xWin()){
            printBoard();
            oPlayer();
        }
    }
    if(xWin()){
        System.out.print("Player X is the winner");
    }
    else{
        System.out.print("Player O is the winner");
    }

    }//End of Main

    public static void printBoard(){
        System.out.println(board[0][0] + "|" + board[0][1] + "|" + board[0][2]);
        System.out.println(board[1][0] + "|" + board[1][1] + "|" + board[1][2]);
        System.out.println(board[2][0] + "|" + board[2][1] + "|" + board[2][2]);
        System.out.println("-----");
    }

    public static void xPlayer(){
        System.out.println("X: ");
        System.out.println("Row?: ");
        int row = scan.nextInt();  
        System.out.println("Slot?: ");
        int slot = scan.nextInt(); 
        if(board[row-1][slot-1] == '-'){
            board[row-1][slot-1] = 'X';
        }
        else{
            System.out.println("That place is invalid");
            System.out.println("Try Again");
            xPlayer();
        }
    }
    public static void oPlayer(){
        System.out.println("O: ");
        System.out.println("Row?: ");
        int row = scan.nextInt();  
        System.out.println("Slot?: ");
        int slot = scan.nextInt(); 
        if(board[row-1][slot-1] == '-'){
            board[row-1][slot-1] = 'O';
        }
        else{
            System.out.println("That place is invalid");
            System.out.println("Try Again");
            oPlayer();
        }

    }

    public static boolean checkWin(){
        boolean isWin = false;
        if(xWin()){
            isWin = true;
        }
        else if(oWin()){
            isWin = true;
        }
        return isWin;
    }

    public static boolean xWin(){
        if(board[0][0] == 'X' && board[0][1] == 'X' && board[0][2] == 'X'){
            return true;
        }
        else if(board[1][0] == 'X' && board[1][1] == 'X' && board[1][2] == 'X'){
            return true;
        }
        else if(board[2][0] == 'X' && board[2][1] == 'X' && board[2][2] == 'X'){
            return true;
        }

        else if(board[0][0] == 'X' && board[1][1] == 'X' && board[2][2] == 'X'){
            return true;
        }
        else if(board[0][2] == 'X' && board[1][1] == 'X' && board[2][0] == 'X'){
            return true;
        }

        else if(board[0][0] == 'X' && board[1][0] == 'X' && board[2][0] == 'X'){
            return true;
        }
        else if(board[0][1] == 'X' && board[1][1] == 'X' && board[2][1] == 'X'){
            return true;
        }
        else if(board[0][2] == 'X' && board[1][2] == 'X' && board[2][2] == 'X'){
            return true;
        }
        else{
            return false;
        }

    }
    public static boolean oWin(){
        if(board[0][0] == 'O' && board[0][1] == 'O' && board[0][2] == 'O'){
            return true;
        }
        else if(board[1][0] == 'O' && board[1][1] == 'O' && board[1][2] == 'O'){
            return true;
        }
        else if(board[2][0] == 'O' && board[2][1] == 'O' && board[2][2] == 'O'){
            return true;
        }

        else if(board[0][0] == 'O' && board[1][1] == 'O' && board[2][2] == 'O'){
            return true;
        }
        else if(board[0][2] == 'O' && board[1][1] == 'O' && board[2][0] == 'O'){
            return true;
        }

        else if(board[0][0] == 'O' && board[1][0] == 'O' && board[2][0] == 'O'){
            return true;
        }
        else if(board[0][1] == 'O' && board[1][1] == 'O' && board[2][1] == 'O'){
            return true;
        }
        else if(board[0][2] == 'O' && board[1][2] == 'O' && board[2][2] == 'O'){
            return true;
        }
        else{
            return false;
        }

    }


}