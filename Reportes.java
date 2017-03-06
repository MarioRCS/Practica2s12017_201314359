/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package proyecto2;

import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;
import com.sun.java.swing.plaf.windows.WindowsBorders;
import java.awt.Color;
import java.awt.Desktop;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;
import javax.swing.Action;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.border.Border;
import static proyecto2.VentanaLista.webClient;

/**
 *
 * @author Roberto
 */
public class Reportes extends JFrame{
    
    JPanel pan;
    JButton btn1;
    JButton btn2;
    JButton btn3;
    JButton btn4;
    JButton btn5;
    JButton btn6;
    JTextField caja1;
    JTextField caja2;
    public Reportes(){
    
        setBounds(1000,50,300,450);
        setTitle("Ventana Grafos");
        
        pan= new JPanel();
        setContentPane(pan);
        pan.setLayout(null);
        pan.setBackground(Color.lightGray);
        btn1= new JButton("Grafo Lista");
        btn1.setBounds(50,50, 100, 50);
        btn2= new JButton("Grafo Cola");
        btn2.setBounds(160,50, 100, 50);
        
        btn3= new JButton("Grafo Pila");
        btn3.setBounds(50,110, 100, 50);
        btn4= new JButton("Grafo Matriz");
        btn4.setBounds(160,110, 120, 50);
        btn5= new JButton("Grafo por letra");
        btn5.setBounds(30,240, 130, 50);
        btn6= new JButton("Grafo por dominio");
        btn6.setBounds(170,240, 130, 50);
        
        caja1=new JTextField();
        caja1.setBounds(30,180, 100, 50);
        caja2=new JTextField();
        caja2.setBounds(170,180, 100, 50);
        pan.add(btn1);
        pan.add(btn2);
        pan.add(btn3);
        pan.add(btn4);
        pan.add(btn5);
        pan.add(btn6);
        pan.add(caja1);
        pan.add(caja2);
        
        btn1.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                
                 String nombre ="";
                    RequestBody formBody = new FormEncodingBuilder()
                            
                            .add("dato", nombre)
                           
                            .build();
                    
                    String r = getString("metodoWeb11", formBody);
                    //System.out.println(r + "---");
                    
                    Graphviz(r,"C:\\Users\\Roberto\\Desktop\\grafo1.pdf");

try {
     File path = new File ("C:\\Users\\Roberto\\Desktop\\grafo1.pdf");
     Desktop.getDesktop().open(path);
}catch (IOException ex) {
     System.out.println( ex.getMessage());
}
                
         
               
            }
        });
        
        btn2.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                
                String nombre ="";
                    RequestBody formBody = new FormEncodingBuilder()
                            
                            .add("dato", nombre)
                           
                            .build();
                    
                    String r = getString("metodoWeb12", formBody);
                    //System.out.println(r + "---");
                    
                    Graphviz(r,"C:\\Users\\Roberto\\Desktop\\grafo2.pdf");

try {
     File path = new File ("C:\\Users\\Roberto\\Desktop\\grafo2.pdf");
     Desktop.getDesktop().open(path);
}catch (IOException ex) {
     System.out.println( ex.getMessage());
}
                
                
            }
        });
        
        btn3.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                
              String nombre ="";
                    RequestBody formBody = new FormEncodingBuilder()
                            
                            .add("dato", nombre)
                           
                            .build();
                    
                    String r = getString("metodoWeb13", formBody);
                    //System.out.println(r + "---");
                    
                    Graphviz(r,"C:\\Users\\Roberto\\Desktop\\grafo3.pdf");

try {
     File path = new File ("C:\\Users\\Roberto\\Desktop\\grafo3.pdf");
     Desktop.getDesktop().open(path);
}catch (IOException ex) {
     System.out.println( ex.getMessage());
}
                
                
                
                
            }
        });
        
     btn5.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                
            String nombre =caja1.getText();
                    RequestBody formBody = new FormEncodingBuilder()
                            
                            .add("dato", nombre)
                           
                            .build();
                    
                    String r = getString("metodoWeb15", formBody);
                    //System.out.println(r + "---");
                    
                    Graphviz(r,"C:\\Users\\Roberto\\Desktop\\grafo5.pdf");

try {
     File path = new File ("C:\\Users\\Roberto\\Desktop\\grafo5.pdf");
     Desktop.getDesktop().open(path);
}catch (IOException ex) {
     System.out.println( ex.getMessage());
}
                
                
              
            }
        });
        
    }
     public  String getString(String metodo, RequestBody formBody) {

        try {
            URL url = new URL("http://127.0.0.9:5000/" + metodo);
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            //java.util.logging.Logger.getLogger(proyecto2.TestWebServer.class.getName()).log(Level.SEVERE, null, ex);
            System.out.println(ex.getMessage());
        } catch (Exception ex) {
            //java.util.logging.Logger.getLogger(proyecto2.TestWebServer.class.getName()).log(Level.SEVERE, null, ex);
        System.out.println(ex.getMessage());
        }
        return null;
    }
     
     
      public void Graphviz(String path,String path2){
   // System.out.println("Hola Mundo");
    try {
      
      String dotPath = "C:\\Program Files (x86)\\Graphviz2.38\\bin\\dot.exe";
      
      String fileInputPath = path;
      String fileOutputPath = path2;
      
      String tParam = "-Tpdf";
      String tOParam = "-o";
        
      String[] cmd = new String[5];
      cmd[0] = dotPath;
      cmd[1] = tParam;
      cmd[2] = fileInputPath;
      cmd[3] = tOParam;
      cmd[4] = fileOutputPath;
                  
      Runtime rt = Runtime.getRuntime();
      
      rt.exec( cmd );
    
    } catch (Exception ex) {
      System.out.println( ex.getMessage());
    } finally {
    }

  }
}
