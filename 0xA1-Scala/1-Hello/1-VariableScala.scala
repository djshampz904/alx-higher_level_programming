object VariableScala {
  def main(args: Array[String]): Unit = {
    val firstVariable: Int = 5
    var changeVariable: Int = 10

    printf("Initial value of changed variable %d\n", changeVariable)
    printf("Current value of changed variable %d\n", changeVariable + 1)
    print(firstVariable)
  }
}
