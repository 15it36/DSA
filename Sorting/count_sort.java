import java.util.*;


class CountSort{

	static void sort(int[] arr, int size)
	{
		int max = Arrays.stream(arr).max().getAsInt();
		int min = Arrays.stream(arr).min().getAsInt();
		int range = (max - min) + 1;
		System.out.println();
		int[] output = new int[size];
		int[] count_arr = new int[range];

		for(int i = 0; i < size; i++)
		{
			count_arr[arr[i] - min]++;
		}

		for(int i = 1; i < count_arr.length; i++)
		{
			count_arr[i] += count_arr[i-1];
		}

		for(int i = size-1; i >= 0; i--)
		{
			output[count_arr[arr[i] - min] - 1] = arr[i];
			count_arr[arr[i] - min]--;
		}

		for(int i = 0; i < size; i++)
		{
			arr[i] = output[i];
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