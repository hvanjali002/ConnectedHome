 #include <stdio.h>
 #include "utilities.h" 
 #include "io.hpp" 
 #include "uart2.hpp" 
 #define DELAY_TIME (1000) // 1000ms 
 #define DELAY_SEC (1 * DELAY_TIME) // second 
 int main() 
 { 
 Uart2& bt_1 = Uart2::getInstance(); 
 bt_1.init(9600); 
 int ls_val = 0; 
 int t_f = 0; 
 char buf[30] = {0}; 
 int m_s = 0; 
 GPIO motion(P2_0); /* Use P1.20 as General Purpose Input/Output (GPIO) */ 
 motion.setAsInput(); 
 //motion.enablePullUp(); 
 while(1) 
 { 
 ls_val = LS.getPercentValue(); 
 t_f = TS.getFarenheit()*100; //to capture 2 decimals 
 m_s = motion.read(); 
 if(m_s) 
 { 
 LE.on(1); 
 LD.setLeftDigit('0'); 
 LD.setRightDigit('1'); 
 } 
 else 
 { 
 LE.off(1); 
 LD.setNumber(t_f/100); 
 } 
 snprintf(buf, sizeof(buf), "ch:mc1,ls:%d,ts:%d,ms:%d", ls_val, t_f, m_s); 
 bt_1.putline(buf); 
 delay_ms(DELAY_SEC); 
 } 
 return 0; 
 } 


