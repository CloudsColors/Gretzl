package com.sep.gretzl;

/**
 * Hello world!
 *
 */
public class Gretzl 
{
    private String className;
    public static void main( String[] args )
    {
        /* 
        For testing the filewriter
        Gretzl gretzlLogger = new Gretzl("Gretzl");
        gretzlLogger.log("main(String[] args) returns void"); // => Gretzl.main(String[] args) returns void 
        */
    }

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
            FileWriter myWriter = new FileWriter("breadcrumbs.txt", true);
            myWriter.append(msg + "\n");                                                                                                                                                                    
            myWriter.close();
        } catch (IOException e) {
            System.err.println(e.getMessage());
            e.printStackTrace();
        }
    }
}
