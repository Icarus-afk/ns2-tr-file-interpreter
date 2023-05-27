#初始化设定
BEGIN {

        sendLine = 0;
        recvLine = 0;
        fowardLine = 0;
        if(mseq==0)
		mseq=10000;
	for(i=0;i<mseq;i++){
		rseq[i]=-1;
		sseq[i]=-1; 
	}
}
#应用程序接收包
$0 ~/^s.* AGT/ {
#	if(sseq[$6]==-1){
        	sendLine ++ ;
#       	sseq[$6]=$6;
#	}
}

 
#应用程序发送包
$0 ~/^r.* AGT/{
#	if(rreq[$6]==-1){
        	recvLine ++ ;
#        	sseq[$6]=$6;
#        }

}

 
#路由程序转发包
$0 ~/^f.* RTR/ {

        fowardLine ++ ;

}
 
#最后输出结果 
END {
        printf "%.4f \n",(recvLine/sendLine);

}