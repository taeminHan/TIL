package com.boj;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class boj_10828 {

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int count = Integer.parseInt(br.readLine());
        List<String> answer = new ArrayList<>();
        for (int i=0;i<count;i++){
            String[] line = br.readLine().split(" ");
            String cmd = line[0];
            switch(cmd){
                case "push":
                    answer.add(line[1]);
                    break;

                case "pop":
                    if (answer.isEmpty()) System.out.println("-1");
                    else System.out.println(answer.remove(answer.size() - 1));
                    break;

                case "size":
                    System.out.println(answer.size());
                    break;

                case "empty":
                    System.out.println(answer.isEmpty() ? "1" : "0");
                    break;

                case "top":
                    if (answer.isEmpty()) System.out.println("-1");
                    else System.out.println(answer.get(answer.size() - 1));
                    break;
            }

        }
    }
}