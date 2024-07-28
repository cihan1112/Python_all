def print_bigA():
   print(" ")
   print("           ** ")
   print("         **   * ")
   print("       **     * ")
   print("    *****")
   print("    *          **")
   print("    *          **")
   print("    *          **")
   print("   *          *")

print("Привет!")
ans = input("Ты любишь программировать?")
if ans == "да":
  print_bigA()
  print("мы подружимся!")
else:
  if ans == "нет":
      print_bigA()
      print("Ну как же так...")
  else:
      print("не понял...")
      print("зато я умею писать большую А, смотри:")
      print_bigA()