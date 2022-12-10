package com.example.calculator

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.TextView
import android.widget.Toast
import java.lang.ArithmeticException

class MainActivity : AppCompatActivity() {
    var lastDigit = false
    var lastDot = false
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

    }
    fun onClickAny(view : View){
//        Toast.makeText(this, "b", Toast.LENGTH_SHORT).show()
        val text = findViewById<TextView>(R.id.operation)
        text.append((view as Button).text)
        lastDigit = true
    }
    fun clr(view: View){
        val text = findViewById<TextView>(R.id.operation)
        text.text = ""
        lastDigit = false
        lastDot = false
    }
    fun doDot(view: View){
        if(lastDigit && !lastDot){
            val text = findViewById<TextView>(R.id.operation)
            text.append((view as Button).text)
            lastDot = true

        }
    }
    fun doAO(view: View){
        val text = findViewById<TextView>(R.id.operation)
        if(lastDigit && !checkAO(text.text.toString())){
            text.append((view as Button).text)
            lastDot = false
            lastDigit = false
        }
    }

    private fun checkAO(txt : String) : Boolean{
        return if(txt.startsWith("-")){
            false
        }else{
            txt.contains("/") || txt.contains("*") || txt.contains("+") || txt.contains("-")
        }
    }
    private fun removeZero(data : String): String{
        var result = data
        if(data.contains(".0")){
            result = data.substring(0, data.length-2)
        }
        return result
    }

    fun onEqual(view: View){
        if(lastDigit){
            val text = findViewById<TextView>(R.id.operation)
            var txt = text.text.toString()
            var prefix = ""
            try{
                if(txt.startsWith("-")) {
                        prefix = "-"
                        txt = txt.substring(1)
                    }


//                ------------------- Divide -----------------------

                if(txt.contains("/")){
                    val splitedData = txt.split("/")
                    var first = splitedData[0]
                    var second = splitedData[1]
                    if(!prefix.isEmpty()){
                        first = prefix + first
                    }
                    var final = removeZero((first.toDouble() / second.toDouble()).toString())
                    text.text = final
                }

//                --------------------- Multiply --------------------

                else if(txt.contains("*")){
                    val splitedData = txt.split("*")
                    var first = splitedData[0]
                    var second = splitedData[1]
                    if(!prefix.isEmpty()){
                        first = prefix + first
                    }
                    var final = removeZero((first.toDouble() * second.toDouble()).toString())
                    text.text = final
                }

//                --------------- addition ----------------------

                else if(txt.contains("+")){
                    val splitedData = txt.split("+")
                    var first = splitedData[0]
                    var second = splitedData[1]
                    if(!prefix.isEmpty()){
                        first = prefix + first
                    }
                    var final = removeZero((first.toDouble() + second.toDouble()).toString())
                    text.text = final
                }

//                ----------------- Subtraction ---------------------

                else if(txt.contains("-")){
                    val splitedData = txt.split("-")
                    var first = splitedData[0]
                    var second = splitedData[1]
                    if(!(prefix.isEmpty())){
                        first = prefix + first
                    }
                    var final = removeZero((first.toDouble() - second.toDouble()).toString())
                    text.text = final
                }

            }catch (e: ArithmeticException){
                e.printStackTrace()
            }

        }
    }



}