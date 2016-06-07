# React Fundamentals Notes

### Class Component and Stateless Function Component
A **class component** can have state. And the **stateless function component** will not have state.

#### Class Component
```js
class App extends React.Component {
	render() {
		return <div>Hello</div>;
	}
}
```

#### Stateless function component

```js
const App = () => <h1>Hello
</h1>
```

### The `render` method
Will only allow to return a single node. It returns `React.createElement`.
