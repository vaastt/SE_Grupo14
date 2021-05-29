package com.example.switchactivities;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {

    private Button goToActivityTwo;
    private Button goToActivityThree;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        goToActivityTwo = findViewById(R.id.activity_main_goToActivityTwo);
        goToActivityTwo.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                changeActivitySecond("https://media.geeksforgeeks.org/wp-content/uploads/20201217163353/Screenrecorder-2020-12-17-16-32-03-350.mp4");
            }
        });

        goToActivityThree = findViewById(R.id.activity_main_goToActivityThree);
        goToActivityThree.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                changeActivityThird();
            }
        });

    }


    private void changeActivitySecond(String video) {
        Intent intent = new Intent(this, SecondActivity.class);
        String videoURL = video;
        intent.putExtra("sentVideoURL", videoURL);
        startActivity(intent);
    }

    private void changeActivityThird() {
        Intent intent = new Intent(this, ThirdActivity.class);
        startActivity(intent);
    }
}