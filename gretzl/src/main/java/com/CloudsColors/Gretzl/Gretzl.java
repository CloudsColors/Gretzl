package com.CloudsColors.Gretzl;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Paths;

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
     * Writes 
     * @param msg what to put in the txt
     */
    private void writeToFile(String msg) {
        try {
            FileWriter myWriter = new FileWriter("breadcrumbs.dot", true);
            System.out.println(Paths.get("breadcrumbs.dot").getFileName().toString());
            if(Paths.get("breadcrumbs.dot").getFileName().toString() == "breadcrumbs.dot"){
                myWriter.append(" -> " + msg + "}", posOfLastChar(), posOfLastChar()+5+msg.length());                                                                                                                                                       
                myWriter.close();
            } else {
                myWriter.append("digraph breadcrumbs {");
                myWriter.append(msg + "}");
                myWriter.close();
            } 
        } catch (IOException e) {
            System.err.println(e.getMessage());
            e.printStackTrace();
        }
    }

    private int posOfLastChar() throws IOException{
        BufferedReader in = new BufferedReader(new FileReader("breadcrumbs.dot"));
        String temp = in.readLine();
        in.close();
        return temp.lastIndexOf(temp);
    }
}
