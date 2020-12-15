package com.CloudsColors.Gretzl;

import java.io.FileWriter;
import java.io.IOException;

public class Gretzl 
{
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
        writeToFile(message);
    }

    /**
     * 
     * @param msg what to put in the txt
     */
    private void writeToFile(String msg) {
        try {
            FileWriter myWriter = new FileWriter("breadcrumbs.dot", true);
            myWriter.append(msg + " -> ");                                                                                                                                                                    
            myWriter.close();
        } catch (IOException e) {
            System.err.println(e.getMessage());
            e.printStackTrace();
        }
    }
}
