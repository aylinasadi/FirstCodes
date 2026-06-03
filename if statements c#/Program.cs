Console.WriteLine("Please enter your age: ");
int age = Convert.ToInt32(Console.ReadLine());

if (age > 100)
{
    Console.WriteLine("You are too old to sign up!");
}
else if (age >= 18)
{
    Console.WriteLine("You are allowed to sign up!");
}
else if (age < 0)
{
    Console.WriteLine("You don't exist yet!");
}
else
{
    Console.WriteLine("You must be 18+ to sign up!");
}

Console.WriteLine("Please enter your name: ");
String name = Console.ReadLine();

if (name == "")
{
    Console.WriteLine("You have to enter your name!");
}
else
{
    Console.WriteLine("Hello " + name + "!");
}

/*
 * if (name != "")       the != mean "not"
 * {
 *    Console.WriteLine("Hello " + name);
 * }
 * else
 * {
 *    Console.WriteLine("You have to enter your name!");
 * }
 */


    Console.ReadKey();