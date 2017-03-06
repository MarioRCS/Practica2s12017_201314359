/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package proyecto2;

import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.Action;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;

/**
 *
 * @author Roberto
 */
public class Ventana extends JFrame {
    
    JPanel pan;
    JButton btn1;
    JButton btn2;
    JButton btn3;
    JButton btn4;
    public Ventana(){
        setTitle("Ventna Principal");
        setBounds(550,120,300,450);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        pan= new JPanel();
        setContentPane(pan);
        setResizable(false);
        pan.setLayout(null);
        pan.setBackground(Color.LIGHT_GRAY);
        btn1= new JButton("Lista");
        btn1.setBounds(40, 50,200, 75);
        btn2= new JButton("Matriz Dispersa");
        btn2.setBounds(40, 130,200, 75);
        btn3= new JButton("Cola");
        btn3.setBounds(40, 210,200, 75);
        btn4= new JButton("Pila");
        btn4.setBounds(40, 290,200, 75);
        pan.add(btn1);
        pan.add(btn2);
        pan.add(btn3);
        pan.add(btn4);
        
        btn1.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
               VentanaLista v = new VentanaLista();
               v.setVisible(true);
                
                
            }
        });
        
        btn2.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                
               VentanaMatriz vm= new VentanaMatriz();
               vm.setVisible(true);
            }
        });
    
        
        btn3.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                VentanaCola vc= new VentanaCola();
                vc.setVisible(true);
                
            }
        });
        
        
        btn4.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
               VentanaPila vp = new VentanaPila();
               vp.setVisible(true);
                
            }
        });
    }
   
    
}
