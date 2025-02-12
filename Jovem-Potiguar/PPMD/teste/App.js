import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Dimensions, Image } from 'react-native';
import { useState } from "react";
import tw from 'twrnc';
import Publicar from './componentes/Publicar'; 
import Postagem from './componentes/postagem';

export default function App() {
  const [posts, setPosts] = useState([])
  return (
    <View style={[tw`flex gap-5 w-[50%] p-4 items-center mx-auto`]}> 
      {posts.map((post, i) => <Postagem post={post} key={i}/>)}
      <View style={tw`flex flex-row items-center gap-2 border-2 p-2 rounded-full border-black w-[40%]`}>
        <Publicar action= {(post)=>setPosts([...posts, post])}/>
      </View>
    </View>
        
  );
}