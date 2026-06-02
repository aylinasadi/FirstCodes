int apples = 5;

apples = apples + 3;  //standard
//apples += 3;  shortcut
//apples++;  loops

int oranges = 4;

//oranges = oranges - 2;
//oranges -= 2;
oranges--;

int bananas = 6;

//bananas = bananas * 2;
bananas *= 2;

double hours = 7;
//hours = hours / 2;
hours /= 2;

int people = 8;
int remainder = people % 3;

Console.WriteLine(apples);
Console.WriteLine(oranges);
Console.WriteLine(bananas);
Console.WriteLine(hours);
Console.WriteLine(remainder);

Console.ReadKey();