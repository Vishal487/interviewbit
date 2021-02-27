#include <iostream>
using namespace std;

void printArray(int *arr, int n)
{
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
}

void insertionSort(int *arr, int n)
{
    for (int i = 1; i < n; i++)
    {
        int value = arr[i];
        int index = i;
        while (index > 0 && arr[index - 1] > value)
        {
            arr[index] = arr[index - 1];
            index = index - 1;
        }
        arr[index] = value;
    }
}

int main()
{
    int arr[] = {5, 3, 14, 6, 8};
    int n = sizeof(arr) / sizeof(arr[0]);
    printArray(arr, n);
    cout << "\n";

    insertionSort(arr, n);
    printArray(arr, n);
    cout << "\n";
}