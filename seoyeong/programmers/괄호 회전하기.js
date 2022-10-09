function solution(s) {
    var answer = 0;
    let len = s.length;
    for(let i=0;i<len;i++){
        // rotate
        s = s + s[0];
        s = s.slice(1);
        
        // check
        let st = [];
        let flag = false;
        for(let j=0;j<s.length;j++){
            if(s[j] == '['){
                st.push(s[j]);
                flag = true;
            }
            else if(s[j] == '{'){
                st.push(s[j]);
                flag = true;
            }
            else if(s[j] == '('){
                st.push(s[j]);
                flag = true;
            }
            else if(s[j] == ']'){
                if(st.length && st[st.length - 1] == '[')st.pop();
            }else if(s[j] == '}'){
                if(st.length && st[st.length - 1] == '{')st.pop();
            }else if(s[j] == ')'){
                if(st.length && st[st.length - 1] == '(')st.pop();
            }
        }
        if(!st.length && flag)answer++;
    }
    return answer;
}
