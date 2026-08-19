public class HeapSort {

  
    public static void heapify(int[] a, int n, int i) {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;

 
        if (left < n && a[left] > a[largest]) {
            largest = left;
        }

        if (right < n && a[right] > a[largest]) {
            largest = right;
        }

  
        if (largest != i) {
            int temp = a[i];
            a[i] = a[largest];
            a[largest] = temp;

            heapify(a, n, largest);
        }
    }

   
    public static void heapSort(int[] a, int n) {

       
        for (int i = n / 2 - 1; i >= 0; i--) {
            heapify(a, n, i);
        }

        for (int i = n - 1; i > 0; i--) {
            int temp = a[0];
            a[0] = a[i];
            a[i] = temp;

            heapify(a, i, 0);
        }
    }

    public static void main(String[] args) {

        int[] a = {20, 10, 30, 5, 15};
        int n = a.length;

        heapSort(a, n);

        System.out.print("Sorted array: ");

        for (int i = 0; i < n; i++) {
            System.out.print(a[i] + " ");
        }
    }
}