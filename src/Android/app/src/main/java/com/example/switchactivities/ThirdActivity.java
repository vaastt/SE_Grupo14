package com.example.switchactivities;

import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import org.w3c.dom.ls.LSOutput;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;

public class ThirdActivity extends AppCompatActivity implements MyRecyclerViewAdapter.ItemClickListener {

    private Button buttonGoBack;
    private Button buttonWatchVideo;
    private RecyclerView RVOne;
    MyRecyclerViewAdapter adapter;
    private List<String> names = new ArrayList<>();


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_third);


        new AsyncTask<Void, Integer, List<String>>() {
            protected List<String> doInBackground(Void ... voids) {

                try {
                    URL url = new URL("https://www.dcc.fc.up.pt/~michel/passwd");
                    BufferedReader in = new BufferedReader(new InputStreamReader(url.openStream()));
                    String str;
                    while ((str = in.readLine()) != null) {
                        names.add(str);
                    }
                    in.close();

                } catch (Exception e) {
                    e.printStackTrace();
                }

                return names;
            }

            protected void onProgressUpdate(Integer... progress) {
            }

            protected void onPostExecute(List<String> names) {
                consume(names);
            }
        }.execute();

        buttonGoBack = findViewById(R.id.activity_three_goBack);
        buttonGoBack.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                finish();
            }
        });


        //RVOne = findViewById(R.id.rvVideos);



       /* buttonWatchVideo = findViewById(R.id.activity_watch_video);
        RecyclerView recyclerView = findViewById(R.id.rvAnimals);
        buttonWatchVideo = recyclerView.findViewById(R.id.activity_watch_video);

        System.out.println("era uma vez um butao " +         buttonWatchVideo.getId());
*/
          /*buttonWatchVideo.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
               // changeActivitySecond("abc");
            }
        });*/


    }

    protected void consume(List<String> names) {
        RecyclerView recyclerView = findViewById(R.id.rvVideos);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));
        adapter = new MyRecyclerViewAdapter(this, names);
        adapter.setClickListener(this);
        recyclerView.setAdapter(adapter);
    }


    @Override
    public void onItemClick(View view, int position) {
        Toast.makeText(this, "You clicked " + adapter.getItem(position) + " on row number " + position, Toast.LENGTH_SHORT).show();
    }


    private void changeActivitySecond(String video) {
        Intent intent = new Intent(this, SecondActivity.class);
        String videoURL = video;
        intent.putExtra("sentVideoURL", videoURL);
        startActivity(intent);
    }


}




