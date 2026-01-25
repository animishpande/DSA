using System.Collections;

class Example
{
    public static void Main()
    {
        // STACK DATA STRUCTURE IMPLEMENTATION
        // Stack is a LIFO Data structure
        // LIFO stands for Last In First Out - Last element is removed first and first element is removed last (Like a stack of plates)
        // Stack applications:
        // Undo/Redo Functionality, Word Reversal, Stack back/forward on browsers, Backtracking algorithms, Bracket verifications        
        Stack<string> strings = new Stack<string>();
        // Pushing element to a stack
        strings.Push("Hello");
        strings.Push("World");
        strings.Push("I am Animish!");
        // Check the number of elements in a stack
        Console.WriteLine("Count of stack: {0}", strings.Count);
        // A stack can be enumerated without disturbing its contents
        foreach (string val in strings)
        {
            Console.WriteLine("Value: {0}", val);
        }
        // Popping element from a stack
        Console.WriteLine("\nPopping '{0}", strings.Pop());
        // Peek an element in the stack
        Console.WriteLine("Peek at the next element to pop: {0}", strings.Peek());

        // We can create a copy of the stack by converting the first stack into an array using .ToArray() method
        Stack<string> stringsCopy = new Stack<string>(strings.ToArray());
        foreach (string val in stringsCopy)
        {
            Console.WriteLine("Values copy: {0}", val);
        }

        // QUEUE DATA STRUCTURE IMPLEMENTATION
        // Queue is a FIFO data structure. FIFO stands for First In First Out, like a queue for a bus
        Queue<string> myQ = new Queue<string>();
        myQ.Enqueue("Hello");
        myQ.Enqueue("World");
        myQ.Enqueue("I am Animish!");

        // A queue can be enumerated without altering the contents
        Console.WriteLine("\nCount of elements in Queue: {0}", myQ.Count);
        foreach(string val in myQ)
        {
            Console.WriteLine(val);
        }

        // Dequeuing an element from queue
        Console.WriteLine("\nDequeing an element: {0}", myQ.Dequeue());
        // Peek at the next element to dequeue
        Console.WriteLine("Next element is: {0}", myQ.Peek());
        // A queue can be copied in the same way a stack was copied, by converting it to an array
        // To clear a queue, call the clear method
        myQ.Clear();
        Console.WriteLine("Count of Queue after clearing: {0}", myQ.Count);


        // LINKEDLIST IMPLEMENTATION
        // Linked list is a data structure where each node has a value and link to the next node
        // There are mainly three types of LL -> Singly LL, Doubly LL and Circular LL
        
    }
}