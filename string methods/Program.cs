String fullname = "Aylin Asadi";

fullname = fullname.ToUpper(); //all uppercase
//fullname = fullname.ToLower(); all lowercase

String phonenumber = "111-222-3333";

phonenumber = phonenumber.Replace("-", "_");

String username = fullname.Insert(0, "@");

String firstname = fullname.Substring(0, 5); //only the first 5 charachters of fullname
String lastname = fullname.Substring(6, 5);

Console.WriteLine(fullname);
Console.WriteLine(phonenumber);
Console.WriteLine(username);
Console.WriteLine(fullname.Length);
Console.WriteLine(firstname);
Console.WriteLine(lastname);


Console.ReadKey();
