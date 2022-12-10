package com.example.roomautomation

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import com.google.firebase.database.FirebaseDatabase
import com.google.firebase.database.ktx.database
import com.google.firebase.ktx.Firebase

var r1 = "0"
var r2 = "0"
var r3 = "0"
var r4 = "0"
var a = 0
var b = 0
var c = 0
var d = 0
var x = 0

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val b1 = findViewById<Button>(R.id.relay1)
        val b2 = findViewById<Button>(R.id.relay2)
        val b3 = findViewById<Button>(R.id.relay3)
        val b4 = findViewById<Button>(R.id.relay4)

        val l1 = findViewById<TextView>(R.id.textView)
        val l2 = findViewById<TextView>(R.id.textView2)
        val l3 = findViewById<TextView>(R.id.textView3)
        val l4 = findViewById<TextView>(R.id.textView4)

        ma()


        val database = Firebase.database
        b1.setOnClickListener() {
            ma()
            if(a == 0) {
                if(r1 == "0"){
                    x = 1
                }
                else if(r1 == "1"){
                    x = 0
                }
                a = 1
            }

            else if(a == 1) {
                if(r1 == "0"){
                    x = 1
                }
                else if(r1 == "1"){
                    x = 0
                }
                a = 0
            }
            val myRef = database.getReference("relay1")
            myRef.setValue(x)
            ma()
            l1.text = r1

        }
        b2.setOnClickListener() {
            ma()
            if(a == 0) {
                if(r2 == "0"){
                    x = 1
                }
                else if(r2 == "1"){
                    x = 0
                }
                a = 1
            }

            else if(a == 1) {
                if(r2 == "0"){
                    x = 1
                }
                else if(r2 == "1"){
                    x = 0
                }
                a = 0
            }
            val myRef = database.getReference("relay2")
            myRef.setValue(x)
            ma()
            l2.text = r2
        }
        b3.setOnClickListener() {
            ma()
            if(a == 0) {
                if(r3 == "0"){
                    x = 1
                }
                else if(r3 == "1"){
                    x = 0
                }
                a = 1
            }

            else if(a == 1) {
                if(r3 == "0"){
                    x = 1
                }
                else if(r3 == "1"){
                    x = 0
                }
                a = 0
            }
            val myRef = database.getReference("relay3")
            myRef.setValue(x)
            ma()
            l3.text = r3
        }

        b4.setOnClickListener() {
            ma()
            if(a == 0) {
                if(r4 == "0"){
                    x = 1
                }
                else if(r4 == "1"){
                    x = 0
                }
                a = 1
            }

            else if(a == 1) {
                if(r4 == "0"){
                    x = 1
                }
                else if(r4 == "1"){
                    x = 0
                }
                a = 0
            }
            val myRef = database.getReference("relay4")
            myRef.setValue(x)
            ma()
            l4.text = r4
        }


    }

    private fun ma() {
        val database1 = FirebaseDatabase.getInstance().getReference()
        database1.get().addOnSuccessListener {
            r1 = it.child("relay1").value.toString()
            r2 = it.child("relay2").value.toString()
            r3 = it.child("relay3").value.toString()
            r4 = it.child("relay4").value.toString()
        }
    }


}