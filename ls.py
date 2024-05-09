public class LinearSearchProg {
    public static void demo(integer key){
        system.debug('Linear Search');
        integer s = -1;
        List<integer> lst= new List<integer>();
        lst.add(2);
        lst.add(3);
        lst.add(7);
        lst.add(8);
        system.debug('List '+lst);
        for(integer i=0;i<lst.size();i++){
            if(key == lst[i]){
                 s = 1;
            }
        }
        if(s==1){
            system.debug('element found');
        }
        else{
            system.debug('element not found');
        }
    }
}
