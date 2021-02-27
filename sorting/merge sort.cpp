#include <iostream>

using namespace std;

void printArray(int *arr, int n)
{
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
}

void merge(int *arr, int start, int mid, int end)
{
    int temp[end - start + 1];
    int i = start, j = mid + 1;
    int k = 0;

    while (i <= mid && j <= end)
    {
        if (arr[i] < arr[j])
        {
            temp[k++] = arr[i++];
        }
        else
        {
            temp[k++] = arr[j++];
        }
    }
    while (i <= mid)
    {
        temp[k++] = arr[i++];
    }
    while (j <= end)
    {
        temp[k++] = arr[j++];
    }

    for (i = start; i <= end; i++)
    {
        arr[i] = temp[i - start];
    }
}

void mergeSort(int *arr, int start, int end)
{
    if (start < end)
    {
        int mid = (start + end) / 2;
        mergeSort(arr, start, mid);
        mergeSort(arr, mid + 1, end);
        merge(arr, start, mid, end);
    }
}

int main()
{
    int arr[] = {5, 3, 14, 6, 8, 20};
    int n = sizeof(arr) / sizeof(arr[0]);
    printArray(arr, n);
    cout << "\n";

    mergeSort(arr, 0, n - 1);

    printArray(arr, n);
    cout << "\n";
}