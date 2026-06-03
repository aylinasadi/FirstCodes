//a^2 + b^2 = c^2
Console.WriteLine("Enter side A: ");
double A = Convert.ToDouble(Console.ReadLine());

Console.WriteLine("Enter side B: ");
double B = Convert.ToDouble(Console.ReadLine());

double C = Math.Sqrt((A * A) + (B * B));

Console.WriteLine("The hypotenuse is: " + C);

Console.ReadKey();

