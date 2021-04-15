/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.escom.relojmaestro;

import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

/**
 *
 * @author emime
 */
public class GUI implements ActionListener{
    
    public GUI() {
        JFrame frame = new JFrame();
        
        JLabel lblR1 = new JLabel("00:00:00");
        JLabel lblR2 = new JLabel("00:00:00");
        JLabel lblR3 = new JLabel("00:00:00");
        JButton btnModificarR1 = new JButton("Modificar");
        btnModificarR1.addActionListener(this);
        JButton btnModificarR2 = new JButton("Modificar");
        JButton btnModificarR3 = new JButton("Modificar");
        JButton btnEnviarR1 = new JButton("Enviar");
        JButton btnEnviarR2 = new JButton("Enviar");
        JButton btnEnviarR3 = new JButton("Enviar");
        
        JPanel panel = new JPanel();
        panel.setBorder(BorderFactory.createEmptyBorder(70,70,10,10));
        panel.setLayout(new GridLayout(0,1));
        panel.add(btnModificarR1);
        panel.add(btnEnviarR1);
        panel.add(lblR1);
        panel.add(btnModificarR2);
        panel.add(btnEnviarR2);
        panel.add(lblR2);
        panel.add(btnModificarR3);
        panel.add(btnEnviarR3);
        panel.add(lblR3);
        
        frame.add(panel, BorderLayout.CENTER);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setTitle("Practica 2");
        frame.pack();
        frame.setVisible(true);
    }
    
    
    public static void main(String[] args) {
        new GUI();
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        
    }
}
