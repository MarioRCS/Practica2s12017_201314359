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
import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextField;
import static proyecto2.VentanaLista.webClient;

/**
 *
 * @author Roberto
 */
public class VentanaCola extends JFrame{
  
    JPanel pan;
    JTextField  caja1;
  
  
 
    JButton btn1;
    JButton btn2;
    

    public VentanaCola(){
        
        setTitle("Ventna Cola");
        setBounds(550,120,300,260);
        pan= new JPanel();
        setContentPane(pan);
        btn1=new JButton("queue");
        btn1.setBounds(100,100,110,30);
        btn2=new JButton("dequeue");
        btn2.setBounds(100,140,110,30);
       
        setResizable(false);
        pan.setLayout(null);
        pan.setBackground(Color.LIGHT_GRAY);
        caja1= new JTextField();
        caja1.setBounds(40,40,200, 30);

        pan.add(caja1);

        pan.add(btn1);
        pan.add(btn2);
   
     
        caja1.setFocusable(true);
       
        btn1.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
               
                try {
                    String nombre = caja1.getText();
                    RequestBody formBody = new FormEncodingBuilder()
                            
                            .add("dato", nombre)
                            
                            
                            //.add("dato3","Roberto")
                            .build();
                   
                    //System.out.println(indicelista);
                    //String r = getString("metodoWeb", formBody);
                    //System.out.println(r + "---");
                    URL url = new URL("http://127.0.0.9:5000/" + "metodoWeb7");  
                    Request request = new Request.Builder().url(url).post(formBody).build();
                    try {
                        Response response = webClient.newCall(request).execute();
                    } catch (IOException ex) {
                        Logger.getLogger(VentanaLista.class.getName()).log(Level.SEVERE, null, ex);
                    }
                } catch (MalformedURLException ex) {
                    Logger.getLogger(VentanaLista.class.getName()).log(Level.SEVERE, null, ex);
            
                }
            caja1.setText("");
            }
            
        });
        
     
        btn2.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                    String nombre="";         
                    RequestBody formBody = new FormEncodingBuilder()
                           .add("dato",nombre)
                            .build();
                    
                String r = getString("metodoWeb8", formBody);
                System.out.println(r + "---");    
                
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
    
    
    
    }

