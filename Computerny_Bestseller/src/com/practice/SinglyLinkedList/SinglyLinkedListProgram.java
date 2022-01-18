package com.practice.SinglyLinkedList;

import java.util.LinkedList;

class Node{
    Node next; // указатель на следующий элемент
    int data;  // данные

    public Node(){

    }

    public Node(Node next, int data){
        this.next = next;
        this.data = data;
    }
}

//Однонаправленний звязний список
class SinglyLinkedList{
    int size = 0;
    Node start; // указатель на первый элемент
    Node end; // указатель последний элемент

    public void addToStart(int data){ //добавить спереди
        Node node = new Node(null, data); //создаём новый элемент //инициализируем данные.
        // указатель на следующий элемент автоматически инициализируется как null
        if(start == null){
            start = node;
            end = node;
        }else{
            node.next = start;
            start = node;
        }
        size++;
    }

    public void addToEnd(int data){
        Node node = new Node(null, data);
        if(end == null){
            start = node;
            end = node;
        }else{
            end.next = node;
            end = node;
        }
        size++;
    }

    public void printList(){
        Node current = start;
        while (current != null){
            System.out.print(current);
            current = current.next;
        }
        System.out.println();
    }

    public void addAfter(int prevEl, int nextEl){
        Node current = start;
        while(current != null){
            if(prevEl == current.data){
                Node node = new Node();
                node.data = nextEl;
                node.next = current.next;
                current.next = node;
                //ставимо поточний вказівник на новий, оскільки немає сенсу лищній раз проходитись по ньому.
                current = node;
            }
            current = current.next;
        }
        size++;
    }

    public void deleteElement(int data){
        if(start == null){
            return;
        }
        if(start == end){
            start = null;
            end = null;
            return;
        }

        if(start.data == data){
            start = start.next;
        }

        Node current = this.start; //иначе начинаем искать
        while (current.next != null){ //пока следующий элемент существует
            if(current.next.data == data){ //проверяем следующий элемент
                if(end == current.next){ //если он последний
                    end = current; //то переключаем указатель на последний элемент на текущий
                }
                current.next = current.next.next; //найденный элемент выкидываем
                return; //и выходим
            }
            current = current.next; //иначе ищем дальше
        }
    }
}

public class SinglyLinkedListProgram {
    public static void main(String[] args) {
        SinglyLinkedList l = new SinglyLinkedList();
        for(int i = 0; i<=5; i++){
            l.addToEnd(i);
        }
        l.printList();
        l.addAfter(4, 4);
        l.printList();
    }
}
