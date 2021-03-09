import java.util.*;

class InsertionSort{
	static void sort(int[] arr, int size){
		for(int i = 1;i < size; i++){
			int key = arr[i];
			int j = i - 1;
			while(j >= 0 && key < arr[j]){
				arr[j+1] = arr[j];
				j--;
			}
			arr[j + 1] = key;
		}
	}
	
	public static void main(String[] args){
		Scanner ip = new Scanner(System.in);
		int n = ip.nextInt();
		int[] arr = new int[n];
		for(int i = 0; i < n; i++){
			arr[i] = ip.nextInt();
		}
		sort(arr, n);
		for(int i = 0; i < n; i++){
			System.out.print(arr[i]+" ");
		}
	}
}