package com.example.switchactivities;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.messaging.FirebaseMessaging;
import com.google.firebase.messaging.FirebaseMessagingService;

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

        getToken();
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

    private static final String TAG = "PushNotification";

    private void getToken() {
        FirebaseMessaging.getInstance().getToken().addOnCompleteListener(new OnCompleteListener<String>() {
            @Override
            public void onComplete(@NonNull  Task<String> task) {

                // if task is failed then
                if(!task.isSuccessful()) {
                    Log.d(TAG, "onComplete: Failed to get the Token!");
                }

                // Token
                String token = task.getResult();
                Log.d(TAG, "onComplete: "+token);
            }
        });
    }

}