object AnyScala {
  def main(args: Array[String]): Unit = {
    var myObj: Any = "A string"

    myObj = 5
    println(myObj)
    
    myObj = 1.34
    println(myObj)

    myObj = '0'
    println(myObj)

    myObj = true
    println(myObj)
  }
}
