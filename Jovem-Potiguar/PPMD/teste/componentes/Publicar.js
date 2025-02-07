import { View, TextInput, Button } from "react-native";
import tw from "twrnc";
import { useState } from 'react';

export default function Publicar({action}) {
  const [post, setPost] = useState('')
  return (
    <View style={tw`flex-row items-center w-[80%] p-2 rounded-lg`}>
      {/* Input de texto */}
      <TextInput
        style={[tw`flex-1 p-2 focus:border-blue-300 w-[100%]`, { borderWidth: 0, outlineStyle: "none" }]}
        placeholder="Digite algo..."
        onChangeText={setPost}
        value={post}
      />
      <Button title='Postar' style={tw`rounded-lg`} onPress=
        {(e) => {action(post); setPost('');}}
      />
    </View>
  );
}