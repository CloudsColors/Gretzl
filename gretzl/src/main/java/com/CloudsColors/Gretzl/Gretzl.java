package com.CloudsColors.Gretzl;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.util.LinkedList;

public class Gretzl 
{
    private static LinkedList<String> store = new LinkedList<String>();
    private String className;
    /**
     * 
     * @param className className = The name of the Class
     */
    public Gretzl(String className){
        this.className = className;
    }

    /**
     * 
     * @param functionName functionName = The name of the function to be logged
     */
    public void log(String functionName){
        String message = className + "." + functionName; 
        store.add(message);
        writeToFile(message);
    }

    /**
     * Writes 
     * @param msg what to put in the txt
     */
    private void writeToFile(String msg) {
        BufferedWriter bufWrite;
        try { 
            bufWrite = new BufferedWriter(new FileWriter("breadcrumbs.dot"));
            bufWrite.write("digraph breadcrumbs {");
            for(int i = 0; i < store.size(); i++){
                if(i == store.size()-1){
                    bufWrite.append("\"" + store.get(i) + "\"" + "}");
                }else{
                    bufWrite.append("\"" + store.get(i) + "\"" + " -> ");
                }
            }
            bufWrite.close();
        } catch (Exception e) {
            System.err.println(e.getMessage());
            e.printStackTrace();
        } 
    }
}
