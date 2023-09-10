object TypeCasting {
  def main(args: Array[String]): Unit = {
    val oldType: Long = 847637849
    val newType: Float = oldType


    val oldChar: Char = 'A'
    val newChar: Int = oldChar

    printf("%d\n%f\n", oldType, newType)
    printf("%c\n%d\n", oldChar, newChar)
  }
}
