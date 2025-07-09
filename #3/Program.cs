double a = 3.14159;
int b = Convert.ToInt32(a);

Console.WriteLine(a);
Console.WriteLine(b);
Console.WriteLine(a.GetType());
Console.WriteLine(b.GetType());

int c = 333;
double d = Convert.ToDouble(c) +0.333;

Console.WriteLine(c);
Console.WriteLine(d);
Console.WriteLine(d.GetType());

int e = 777;
String f = Convert.ToString(e);

Console.WriteLine(e);
Console.WriteLine(f);
Console.WriteLine(f.GetType());

String g = "$";
char h = Convert.ToChar(g);

Console.WriteLine(g);
Console.WriteLine(h);
Console.WriteLine(g.GetType());

String i = "False";
bool j = Convert.ToBoolean(i);

Console.WriteLine(i);
Console.WriteLine(j);
Console.WriteLine(j.GetType());


Console.ReadKey();
