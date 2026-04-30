//PBL - Problem Based Learning
//Esse primeiro problema é em Java e o enunciado é o mesmo para todos

//Desafio
//Faça uma programa que calcule o salario a ser transferido
//para outro funcionario
//Para realizar o calculo receba o valor bruto do salario e o adicional dos beneficios
//O Salário a ser transferido é calculado da seguinte maneira:

//(valor bruto do salario - percentual de imposto mediante ao salaro) + adicional dos benficios

//para calcular o percentual de imposto segue as alquotas?

//de R$ 0.00 a R$ 1100.00 = 5.00%
// de R$ 1100.01 a R$ 2500.00 = 10.00%
// Maior que R$ 2500.00 = 15.00%

//Entrada 

//A entrada consiste em vários arquivos de teste, que conterá o valor
//bruto do salário e adicional dos beneficios. Conforme mostrando no exemplo de entrada a seguir.

//Saida

//Para cada arquivo de entrada, tera um arquivo de saida.




import java.util.Scanner;

public class Desafio {
    public static void main(String[] args) {
        //lê os valores de Entrada:
        Scanner leitorDeEntradas = new Scanner(System.in);
        float valorSalario = leitorDeEntradas.nextFloat();
        float valorBeneficio = leitorDeEntradas.nextFloat();
        
        float valorImposto = 0;

        if (valorSalario >= 0 && valorSalario <= 1100) {
            //atribuiu a aliquota de 5% mediante o salario:
            valorImposto = 0.05F * valorSalario;
        }
        //Todo criar  as demais condições para a aliquotas de 10.00% e 15.00%.
        else if (valorSalario >= 1100.01 && valorSalario <= 2500) {
            valorImposto = 0.10F * valorSalario;    
        }
        else {
            valorImposto = 0.15F * valorSalario;  
        }


        //calcula e imprime a saida (com 2 casas decimais):

        float saida = valorSalario - valorImposto + valorBeneficio;
        System.out.println(String.format("%.2F", saida));
        
    }

}


