package quiz.myapp.co.`in`

import android.graphics.Color
import android.graphics.Typeface
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.TextView
import android.widget.Toast
import androidx.core.content.ContextCompat
import kotlinx.android.synthetic.main.activity_quizactivity.*

class Quizactivity : AppCompatActivity(), View.OnClickListener{

    private var currentPosition = 1
    private var questionsList: ArrayList<Quiz>? = null
    private var selectedOptionPosition: Int = 0

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_quizactivity)
        questionsList = constants.getQuestion()
        setQuestion()
        option1.setOnClickListener(this)
        option2.setOnClickListener(this)
        option3.setOnClickListener(this)
        option4.setOnClickListener(this)
        submit_btn.setOnClickListener(this)

    }

    private fun setQuestion(){
        var question: Quiz? = questionsList!![currentPosition-1]
        defaultTextViewBg()
//        val totalQ = questionsList!!.size
        if (currentPosition == questionsList!!.size){
            submit_btn.text = "Finished"
        }else{
            submit_btn.text = "Submit"
        }
        questionText.text = question!!.question
        imageImage.setImageResource(question.image)
        progressBar1.progress = currentPosition
        progressText.text = "$currentPosition"+ "/" + progressBar1.max
        option1.text = question.option1
        option2.text = question.option2
        option3.text = question.option3
        option4.text = question.option4
    }

    private fun defaultTextViewBg(){
        val options =  ArrayList<TextView>()
        options.add(0, option1)
        options.add(1, option2)
        options.add(2, option3)
        options.add(3, option4)
        for(option in options){
            option.setTextColor(Color.parseColor("#7A8089"))
            option.typeface = Typeface.DEFAULT
            option.background = ContextCompat.getDrawable(this, R.drawable.option_bg_notselected)
        }
    }

    private fun selectedOptionBg(tv: TextView, selectedTextView: Int){
        defaultTextViewBg()
        selectedOptionPosition = selectedTextView
        tv.setTextColor(Color.parseColor("#363A43"))
        tv.setTypeface(tv.typeface, Typeface.BOLD)
        tv.background = ContextCompat.getDrawable(this, R.drawable.option_bg_selected)

    }

    private fun answerView(ans: Int?, drawableView: Int){
        when(ans){
            1 ->{
                option1.background = ContextCompat.getDrawable(this, drawableView)
            }
            2 ->{
                option2.background = ContextCompat.getDrawable(this, drawableView)
            }
            3 ->{
                option3.background = ContextCompat.getDrawable(this, drawableView)
            }
            4 ->{
                option4.background = ContextCompat.getDrawable(this, drawableView)
            }

        }
    }

    override fun onClick(p0: View?) {
        when(p0?.id){
            R.id.option1 ->{
                selectedOptionBg(option1, 1)
            }
            R.id.option2 ->{
                selectedOptionBg(option2, 2)
            }
            R.id.option3 ->{
                selectedOptionBg(option3, 3)
            }
            R.id.option4 ->{
                selectedOptionBg(option4, 4)
            }
            R.id.submit_btn ->{
                if (selectedOptionPosition == 0){
                    currentPosition++
                    when{
                        currentPosition <= questionsList!!.size ->{
                            setQuestion()
                        }else->{
                        Toast.makeText(this, "Nacho, tumne quiz complete ke lia", Toast.LENGTH_SHORT).show()
                        }
                    }
                }else{
                    val question = questionsList?.get(currentPosition-1)
                    if (question?.correctAns != selectedOptionPosition){
                        answerView(selectedOptionPosition, R.drawable.incorrect_option_bg)
                    }
                    answerView(question?.correctAns, R.drawable.correct_option_bg)

                    if(currentPosition == questionsList?.size){
                        submit_btn.text = "Finished"
                    }else{
                        submit_btn.text = "Go to next Question"
                    }
                    selectedOptionPosition = 0
                }
            }
        }
    }
}