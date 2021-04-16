package com.escom.relojmaestro;

import javax.swing.*;
import java.awt.*;
import java.time.LocalDateTime;

public class InterfazMaestra extends JFrame{
    private JPanel panel;
    private JLabel titulo;
    private JLabel lbl_1, lbl_2, lbl_3;
    private JLabel reloj_1, reloj_2, reloj_3;
    private JButton modificar_1, modificar_2, modificar_3;
    private JButton enviar_1, enviar_2, enviar_3;

    private Hilo hilo_1, hilo_2, hilo_3;

    public InterfazMaestra(){
        this.setSize(1000,300);
        this.setLocationRelativeTo(null);
        this.setTitle("Reloj Maestro");
        this.setDefaultCloseOperation(EXIT_ON_CLOSE);

        construirElementos();

        this.hilo_1 = new Hilo(0, this.reloj_1);
        this.hilo_1.start();
        this.hilo_2 = new Hilo(1, this.reloj_2);
        this.hilo_2.start();
        this.hilo_3 = new Hilo(2, this.reloj_3);
        this.hilo_3.start();

        this.setVisible(true);
    }

    public String obtenerHoraActual(){
        LocalDateTime locaDate = LocalDateTime.now();

        int hora  = locaDate.getHour();
        int minuto = locaDate.getMinute();
        int segundo = locaDate.getSecond();

        return String.valueOf(hora) + ":" + String.valueOf(minuto) + ":" + String.valueOf(segundo);
    }

    public void construirElementos(){
        panel = new JPanel();
        panel.setLayout(null);
        this.getContentPane().add(panel);

        titulo = new JLabel("Administra los relojes conectados");
        titulo.setFont(new Font("Arial",1,22));
        titulo.setBounds(320,20,500,24);
        panel.add(titulo);

        //Primer reloj

        lbl_1 = new JLabel("Reloj 1");
        lbl_1.setFont(new Font("Arial",0,12));
        lbl_1.setBounds(230,100,400,14);
        panel.add(lbl_1);

        reloj_1 = new JLabel(obtenerHoraActual());
        reloj_1.setFont(new Font("Arial",1,20));
        reloj_1.setBounds(200,150,450,20);
        panel.add(reloj_1);

        modificar_1 = new JButton("Editar");
        modificar_1.setBounds(150,200,80,20);
        panel.add(modificar_1);

        enviar_1 = new JButton("Enviar");
        enviar_1.setBounds(270,200,80,20);
        panel.add(enviar_1);


        //Segundo reloj

        lbl_2 = new JLabel("Reloj 2");
        lbl_2.setFont(new Font("Arial",0,12));
        lbl_2.setBounds(480,100,400,14);
        panel.add(lbl_2);

        reloj_2 = new JLabel("23:59:50");
        reloj_2.setFont(new Font("Arial",1,20));
        reloj_2.setBounds(450,150,450,20);
        panel.add(reloj_2);

        modificar_2 = new JButton("Editar");
        modificar_2.setBounds(400,200,80,20);
        panel.add(modificar_2);

        enviar_2 = new JButton("Enviar");
        enviar_2.setBounds(520,200,80,20);
        panel.add(enviar_2);

        //Tercer reloj

        lbl_3 = new JLabel("Reloj 3");
        lbl_3.setFont(new Font("Arial",0,12));
        lbl_3.setBounds(730,100,400,14);
        panel.add(lbl_3);

        reloj_3 = new JLabel("00:59:50");
        reloj_3.setFont(new Font("Arial",1,20));
        reloj_3.setBounds(700,150,450,20);
        panel.add(reloj_3);

        modificar_3 = new JButton("Editar");
        modificar_3.setBounds(650,200,80,20);
        panel.add(modificar_3);

        enviar_3 = new JButton("Enviar");
        enviar_3.setBounds(770,200,80,20);
        panel.add(enviar_3);
    }
}
