/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package proyecto2;

import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
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
import static proyecto2.TestWebServer.getString;
import static proyecto2.TestWebServer.webClient;
import static proyecto2.VentanaLista.webClient;

/**
 *
 * @author Roberto
 */
public class VentanaMatriz extends JFrame{
    
    JPanel pan;
    JTextField  caja1;
    JTextField  caja2;
    JTextField  caja3;
    JTextField  caja4;
    JButton btn1;
    JButton btn2;
    JButton btn3;
    JButton btn4;
    int indicelista;
       public static OkHttpClient webClient = new OkHttpClient();
    public VentanaMatriz(){
        setTitle("Ventna Matriz");
        setBounds(550,120,300,450);
        pan= new JPanel();
        indicelista=0;
        setContentPane(pan);
        btn1=new JButton("agregar");
        btn1.setBounds(100,50,80,30);
        btn2=new JButton("eliminar");
        btn2.setBounds(100,140,80,30);
        btn3=new JButton("buscar letra");
        btn3.setBounds(75,230,150,30);
        btn4=new JButton("buscar dominio");
        btn4.setBounds(75,330,150,30);
        setResizable(false);
        pan.setLayout(null);
        pan.setBackground(Color.LIGHT_GRAY);
        caja1= new JTextField();
        caja1.setBounds(40,10,200, 30);
        caja2= new JTextField();
        caja2.setBounds(40,90,200, 30);
        caja3= new JTextField();
        caja3.setBounds(40,180,200, 30);
        caja4= new JTextField();
        caja4.setBounds(40,280,200, 30);
        pan.add(caja1);
        pan.add(caja2);
        pan.add(caja3);
        pan.add(caja4);
        pan.add(btn1);
        pan.add(btn2);
        pan.add(btn3);
        pan.add(btn4);
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
                    URL url = new URL("http://127.0.0.9:5000/" + "metodoWeb4");  
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
    
        btn3.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                
                String nombre = caja3.getText();
                    RequestBody formBody = new FormEncodingBuilder()
                            
                            .add("dato", nombre)
                            
                            //.add("dato3","Roberto")
                            .build();
                    
                    
                    String r = getString("metodoWeb5", formBody);
                    System.out.println(r + "---");
                
                
            }
        });
        
        btn4.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                
                String nombre = caja4.getText();
                    RequestBody formBody = new FormEncodingBuilder()
                            
                            .add("dato", nombre)
                            
                            //.add("dato3","Roberto")
                            .build();
                    
                    
                    String r = getString("metodoWeb6", formBody);
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
