package com.gpt;


public class Practice20261017 {

    public static void main(String[] args) {
        Practice20261017 practice = new Practice20261017();

        // 예시 1: 기대 결과 3
        int[] responseTimes = {120, 500, 230, 800, 500};
        int threshold = 500;

        int result = practice.solution(responseTimes, threshold);

        System.out.println("기대 결과: 3");
        System.out.println("실행 결과: " + result);

        // 예시 2: 기대 결과 0
        System.out.println(practice.solution(
                new int[]{100, 200, 300}, 400
        ));

        // 예시 3: 기대 결과 1
        System.out.println(practice.solution(
                new int[]{200}, 200
        ));
    }

    public int solution(int[] responseTimes, int threshold) {

        int count = 0;

        for (int responseTime : responseTimes) {
            if (responseTime >= threshold) {
                count++;
            }
        }
        return count;
    }
}